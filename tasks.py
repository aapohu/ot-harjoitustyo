from invoke import task

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task
def coverage-report(ctx):
    ctx.run("coverage html")