import string


class Settings:
    CHARSPACE = string.ascii_letters + string.digits  # Used to generate the "path" of the full URL.
    SCHEME = "http://"
    HOST = "localhost"  # format: google.com
    PORT = 80
