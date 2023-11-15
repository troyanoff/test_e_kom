from fastapi import FastAPI, status
from pydantic import BaseModel
from tinydb import TinyDB, Query

from validations import check_type


db = TinyDB('db.json')

Form = Query()


app = FastAPI()


class ReqForm(BaseModel):
    info: str | None
    address: str | None
    organization: str | None
    cooperation: str | None


def check_dict_inclusion(dict1, dict2):
    for key, value in dict1.items():
        if key not in dict2 or dict2[key] != value:
            return False
    return True


@app.post('/get_form/', status_code=status.HTTP_200_OK)
def get_form(
    request: ReqForm
):
    result_form = ''
    request = request.model_dump()
    for name, value in request.items():
        request[name] = check_type(value)
    for form in db:
        form = dict(form)
        if check_dict_inclusion(request, form['fields']):
            result_form = form['name']
    if result_form:
        return {'form': result_form}
    else:
        return request.model_dump_json()


@app.get('/get_all/', status_code=status.HTTP_200_OK)
def get_all():
    return {'result': list(db.all())}
