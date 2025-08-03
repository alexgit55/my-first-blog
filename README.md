# my-first-blog

This project is creating my first blog based on the tutorial from djangogirls (https://tutorial.djangogirls.org/en/).

It is creating a blog website using python with django, as well as structuring with html and formatting with css.

## Features
- Create a blog application based on the Django framework in Python
- Customized formatting with html and css
- Save blog posts in an sqlite database
- Ability to create, edit and delete posts directly from application
- Basic authentication to prevent unauthorized creating and editing to blog
- Application is published using Azure App service

## History

8/2/2025 - I've worked on and completed the main tutorial section of this blog tutorial.  It was a lot of fun going through and I feel like I've learned a lot. I learned the basic structure
           of a django applicaton, html, css and how they interact with each other.  For example how you can have html elements perform Python functions. I went through the main tutorial and
           have a published web application. The functionality includes: 
           
- viewing all posts in a list
 - Viewing a single post in detail view
- Making a new post
- Editing a post

The tutorial goes through publishing it to pythonanywhere, but since I already have a Microsoft Azure subscription and I've been learning the
developer certification, I wanted to publish it there. I was able to complete it successfully.  This repository is directly linked to the web app so any changes I work on and push
here, a github action triggers and publishes to the app, which is cool to watch.  Ideally you'd want it to go to a development slot first to verify it looks ok, but this works
well enough for now while learning.  The tutorial has several "extra credit" posts to add more functionality. so I'm going to go through those next. I'm looking forward to it

8/3/2025 - I've started working on the extra credit "homework" sections of the djangogirls tutorial (https://tutorial-extensions.djangogirls.org/en/). The first assignment involves
creating drafts, ability to publish a post, and also delete a post. In the main project, when you create a post, it immediately gets published to the main blog list.  This time around,
when you creating a post, it gets saved as a draft (ie w/o a publish date).  Then we can view the drafts on a draft list page, and publish them once we've reviewed them.  I had to make
a change to the tutorial since my posts were publishing at first.  They talk about using a form with submit button instead of a regular button, but their code doesn't reflect that.  I 
used github copilot to review and was able to get it setup correctly.  I also made a change where when publishing, instead of going to the post_detail page, it refreshes the draft list 
page so I could verify that the post has been removed from drafts. I like this much better so I can see that it was cleared out. The next assignment is going to be making the site more
secure. I'll post here on that next.

Awesome, I've successfully added more security to the site.  This involved adding buttons to login and logout to the top border.  Then the buttons that are used for making changes to the
blog, new/edit/delete, are only visible if you're logged in. As additional security and recommended best practice, i moved the secret key to a separate environment variable instead of 
directly in the source code.  That way it can read the key from the environment that it's running in instead. I feel very accomplished at being able to go through these, with help
of course.
