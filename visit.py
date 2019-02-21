from flask import Flask
import redis

visit_app=Flask(__name__)
redis_client=redis.Redis(host="redis-server")
redis_client.set("visits","0")


@visit_app.route("/")
def start():
    return "Welcome!!!"

@visit_app.route("/getVisitsCount")
def get_visits_count():
    visits=int(redis_client.get("visits"))
    return get_visits_redis(visits)

def get_visits_redis(visits):
    redis_client.set("visits",str(visits+1))
    return "Number of visits: {}".format(visits)

if __name__ == "__main__":
    visit_app.run("0.0.0.0",port=5001, debug=True)
