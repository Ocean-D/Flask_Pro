import requests

class HTTP():


    @staticmethod
    def get(url,return_json =True):
        #return_json 用于返回数据是json 还是text 用三元表达式简洁代码
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if  r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''

