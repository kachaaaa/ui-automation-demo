from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Простая база пользователей
USERS = {"admin": "admin"}

# Шаблон страницы логина
login_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}
    <form method="post">
        <label>Username:</label>
        <input type="text" name="username" />
        <label>Password:</label>
        <input type="password" name="password" />
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

# Шаблон дашборда
dashboard_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <nav id="main-menu">
        <ul>
            <li>Home</li>
            <li>Profile</li>
            <li>Settings</li>
        </ul>
    </nav>
    <table id="data-table">
        <tr><th>ID</th><th>Name</th></tr>
        <tr><td>1</td><td>Item 1</td></tr>
        <tr><td>2</td><td>Item 2</td></tr>
    </table>
</body>
</html>
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if USERS.get(username) == password:
            return redirect(url_for("dashboard"))
        else:
            error = "Неверный логин или пароль"
    return render_template_string(login_html, error=error)

@app.route("/dashboard")
def dashboard():
    return render_template_string(dashboard_html)

if __name__ == "__main__":
    app.run(debug=True)