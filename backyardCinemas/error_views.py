from flask import Flask, render_template

# Create error views, labelled accordingly

# 400 Bad Request

# 401 Unauthorised

# 403 Forbidden


def forbidden(e):
    return render_template('403.html'), 403
# 404 Page Not Found
# @app.errorhandler(404)


def page_not_found(e):
    return render_template('errors/404.html'), 404


# 405 Method Not Allowed

def method_not_allowed(e):
    return render_template('errors/405.html'), 405

# 406 Not Acceptable

# 408 Request Time-Out

# 410 Gone

# 500 Internal Server Error


def interal_server_error(e):
    return render_template('errors/500.html'), 500

# 502 Bad Gateway

# 503 Out of Resources

# 504 Gateway Time-Out

# 505 HTTP Version Not Supported
