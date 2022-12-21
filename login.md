---
title: Log in
...

{% if not user.is_authenticated %}
<form method="post" action="/login">
<div class="form-group">
<label for="password">Password</label>
<input type="password" class="form-control" id="password" name="password" placeholder="Password">
</div>
<button type="submit" class="btn btn-primary">Submit</button>
</form>
{% else %}
You are already logged in.
Click [here](/logout?redirect=/) to log out.
{% endif %}
