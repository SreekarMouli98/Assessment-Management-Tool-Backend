def jwt_response_payload_handler(token, user=None, request=None):
    """
    Custom response payload handler.
    This function controlls the custom payload after login or token refresh. This data is returned through the web API.
    """
    return {
        'token'     : token,
        'is_student': user.is_student,
        'is_mentor' : user.is_mentor,
        'username'  : user.username
    }