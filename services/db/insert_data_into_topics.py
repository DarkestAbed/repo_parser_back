import logging
import pdb

from app.exceptions import NoTopicOnRepo
from services.sqlite import SQLiteDatabase


async def insert_data_into_topics(db: SQLiteDatabase, repo: dict):
    # data def
    query = """
        INSERT INTO 
            topics
            (
                id
                ,url
                ,topic
            )
        VALUES
            (
                :id
                ,:url
                ,:topic
            )
    """
    topics_list = repo["topics"].split(" / ")
    logging.debug(topics_list)
    logging.debug(topics_list[0])
    logging.debug(True if topics_list[0] is "" else False)
    # pdb.set_trace()

    # execution
    if topics_list[0] is "":
        raise NoTopicOnRepo
    for topic in topics_list:
        values_dict = {
            "id": repo["id"],
            "url": repo["url"],
            "topic": topic
        }
        logging.debug(query)
        logging.debug(values_dict)
        # # executing insert
        logging.info(f"Adding data for repo '{repo['name']}'...")
        await db.execute(query=query, values=values_dict)
