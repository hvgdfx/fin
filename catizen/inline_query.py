import requests
from catizen.constant.constant import TOKEN


def handle_inline_query(update):
    inline_query = update["inline_query"]
    query_text = inline_query["query"]
    inline_query_id = inline_query["id"]

    # 构造返回的 inline query 结果
    results = [
        {
            "type": "article",
            "id": "1",
            "title": "Hello",
            "input_message_content": {"message_text": "Hello, world!"},
        },
        {
            "type": "article",
            "id": "2",
            "title": "Bye",
            "input_message_content": {"message_text": "Goodbye, world!"},
        },
    ]

    # 发送 inline query 结果
    url = f"https://api.telegram.org/bot{TOKEN}/answerInlineQuery"
    data = {"inline_query_id": inline_query_id, "results": results}
    response = requests.post(url, json=data)
    print(response.json())


def main():
    # 这里可以监听 webhook 或者使用长轮询方式获取更新
    # 假设 update 是从 webhook 或者长轮询中获取的更新数据
    update = {
        "inline_query": {
            "id": "987654321",
            "from": {
                "id": 123456789,
                "is_bot": False,
                "first_name": "John",
                "last_name": "Doe",
                "username": "johndoe",
                "language_code": "en",
            },
            "query": "search_term",
            "offset": "",
        }
    }

    handle_inline_query(update)


if __name__ == "__main__":
    main()
