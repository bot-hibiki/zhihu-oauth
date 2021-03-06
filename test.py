# -*- coding: utf-8 -*-
import sys
import json
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

from zhihu_oauth import ZhihuClient
from neo4j import Database

client = ZhihuClient()
client.load_token('token.pkl')


# me = client.me()

def user_bestanswers():
    database = Database()
    tx = database.graph.begin()
    topicId = 19554298
    topic = client.topic(topicId)
    answers = topic.best_answers
    i = 0
    for answer in answers:
        # 作者信息
        try:
            author = answer.author
            author_name = author.name
            author_weibo = author.sina_weibo_url if author.sina_weibo_url else ''
            author_email = author.email if author.email else ''
            temp_location = ''
            if author.locations:
                for location in author.locations:
                    temp_location += location.name
            author_location = temp_location
            author_gender = "male" if author.gender ==1 else "female" if author.gender ==2 else "未填"
            author_business = author.business.name if author.business else ""

            temp_education = ''
            if author.educations:
                for education in author.educations:
                    if 'school' in education:
                        temp_education += education.school.name
                    if 'major' in education:
                        temp_education += education.major.name
            author_education = json.dumps(temp_education)

            temp_employment = ''
            if author.employments:
                for employment in author.employments:
                    if 'company' in employment:
                        temp_employment += employment.company.name
                    if 'job' in employment:
                        temp_employment += employment.job.name
            author_employment = json.dumps(temp_employment)

            # 答案信息
            thanks_count = str(answer.thanks_count)
            voteup_count = str(answer.voteup_count)
            comment_count = str(answer.comment_count)
            excerpt = json.dumps(answer.excerpt.replace("\\", "").replace("'", ""))
            # print(answer.excerpt.replace("\\", "").replace("'", ""))

            cypher1 = "merge(u:User{name:'"+author_name+"',email: '"+author_email+"',gender: '"+author_gender+"'," \
                    "weibo: '"+author_weibo+"', loation: '"+author_location+"'," \
                    "business: '"+author_business+"',education: '"+author_education+"'," \
                    "employment: '"+author_employment+"',topicID: '"+str(topicId)+"'}) SET u.id = '"+str(author.id)+"'"
            tx.run(cypher1)
            cypher2 = "merge(a:Answer{excerpt: '"+excerpt+"'," \
                            "thanks_count: "+thanks_count+",voteup_count: "+voteup_count+"," \
                            "comment_count: "+comment_count+",question: '"+answer.question.title+"'}) SET a.id="+str(answer.id)+""
            tx.run(cypher2)
            relationShip1 = "match(u:User{id: '"+str(author.id)+"'}) merge (a:Answer{id:'"+str(answer.id)+"'})  MERGE (u)-[:AUTHOR]->(a)"
            tx.run(relationShip1)
            if i == 0:
                database.graph.data("CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE")
                # database.graph.data("CREATE CONSTRAINT ON (a:Answer) ASSERT a.id IS UNIQUE")
            i += 1
            if len(answers._data) % 20 == 0:
                if i % 20 == 0:
                    print("开始提交!")
                    tx.commit()
                    print("此时answers长度为"+str(len(answers._data)))
                    print("抓取了"+str(i)+"个用户")
                    tx = database.graph.begin()
            else:
                tx.commit()
                print("此时answers长度为"+str(len(answers._data)))
                print("此处answers单次返回长度不为20")
                print("抓取了"+str(i)+"个用户")
                tx = database.graph.begin()
        except Exception, e:
            print(e.message)
            failure = database.graph.begin()
            failure.run("create(f:UserFailure{id:'"+str(author.id)+"',exception:'"+str(e.message)+"'})")
            failure.commit()
            continue
    print("it is over")

def main():
    user_bestanswers()


if __name__ == '__main__':
    main()
