# Overall this is an excellent project.  I added a lot of comments throughout the codebase, but many are stylistic, 
# or me slightly revising some of the patterns I introduced in the sample project.  Feel free to discuss further.

# 1. Remove the api folder, it's unnecessary
# 2. The update functions you wrote in db are really cool.  They can be changed to one function that takes key and value to update. (ask me)
# 3. Change run and run adapters to fit the manage.py structure, and add the entrypoint.sh file
# 4. Add the settings.py file, which references .env (which is in .gitignore)
# 5. Not sure what the tests/adapters/reader.py file is about
# 6. Restructure the frontend, add tests
# 7. test_models.py
    # seems like these functions are testing more the adapter than the model, let's discuss
    # the get_sibling functions are not tested here, and they deserve to be
