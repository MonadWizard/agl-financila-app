import re
from rest_framework import renderers
import json


class UserRenderer(renderers.JSONRenderer):
    def string_error(self, data):
        complete_error = ""
        if "ErrorDetail" in str(data):
            for key, value in data.items():
                single_err = json.dumps(value)
                single_err = re.sub("[^A-Za-z0-9]+", " ", single_err).strip()
                complete_error = complete_error + single_err
            return complete_error
        else:
            return data

    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ""

        complete_error = self.string_error(data)
        if "ErrorDetail" in str(data):

            response = json.dumps({"success": False, "message": complete_error})
        elif renderer_context["response"].status_code == 400:
            response = json.dumps({"success": False, "message": complete_error})
        elif renderer_context["response"].status_code == 401:

            response = json.dumps({"success": False, "message": complete_error})

        elif renderer_context["response"].status_code == 404:
            response = json.dumps({"success": False, "message": complete_error})

        elif renderer_context["response"].status_code == 500:
            response = json.dumps({"success": False, "message": complete_error})

        else:
            response = {"success": True
                        , "message": 'success'}
            response.update(data)
            return json.dumps(response)
        return response
