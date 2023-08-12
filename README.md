# Week 3 assignment

_Python Bootcamp for Data Week 3 assignment_

This week, you learned the basics of Python testing. From a brief overview of the standard library to using a more modern approach with Pytest, one of the most popular testing libraries in Python. You'll use that knowledge to complete the assignment in this repository, where you'll write tests, fix broken tests, and debug issues in real-world code.

> 💡 This template repository is made for GitHub Classroom delivery, but can be used independently if you want to learn on your own.

## Assignment instructions

This repository uses automated grading (or testing). When starting, all automated tests will fail. Your task is to make them all pass.

1. Go to the [tests](./tests) directory and fix the [invalid.py](./tests/invalid.py) so that Pytest automatically collects it.
1. Update the three tests inside [invalid.py](./tests/invalid.py) so that Pytest can run them.
1. Go to the [tests/test_utils.py](./tests/test_utils.py) test file and fix the three tests that aren't passing.
1. Repeat the fix/push/verify cycle until all tests are passing and the [actions](/../../actions) tab shows a green.

> 💡 As part of the GitHub Classroom setup, you might get an automated Pull Request created for direct feedback by your Professor or by the TAs.

**Verify your work** by running `pytest -v` in the root of your repository. If you are using Codespaces, `pytest` will already be installed for you and available for you to run tests that are used for auto-grading. 

## Resources

Use the linked resources in this section to review and reference any of the previously covered content. All questions in this assignment come from content previously covered in the bootcamp course.

### GitHub Copilot 
In this assignment, you'll use [GitHub Copilot](https://github.com/features/copilot). If you are using Codespaces, then the extension is already installed for you. Otherwise you can search for it in extensions on Visual Studio Code, and then install it. 

#### How to get GitHub Copilot for free
If you have an educational email address (usually one that ends on `.edu`) then you can validate your student or faculty status by [following this guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/step-by-step-setting-up-github-student-and-github-copilot-as-an/ba-p/3736279?WT.mc_id=academic-0000-alfredodeza)

### How do I use Copilot
Copilot is an AI-assistive technology that will suggest you completions _that you must verify as correct_. Suggestions are accepted by hitting the `Tab` key. You can also write a _prompt_ as a comment. Suggestions will be generated after you hit the `Enter` or `Return` keys.

Use the [following videos from Microsoft](https://learn.microsoft.com/shows/introduction-to-github-copilot/?WT.mc_id=academic-0000-alfredodeza) as a reference on how to get started.

### Week 3 Reference Content

1. [Introduction to testing](https://github.com/alfredodeza/python-testing/tree/main/notebooks/lesson1)
1. [Writing useful tests]( https://github.com/alfredodeza/python-testing/tree/main/notebooks/lesson2)
1. [Test failures](https://github.com/alfredodeza/python-testing/tree/main/notebooks/lesson3)


### Reading and code resources

- [week 1: Introduction to Python](https://github.com/alfredodeza/introduction-to-python)
- [Week 2: Python Functions and Classes](https://github.com/alfredodeza/python-functions-and-classes)
- [Week 3: Testing In Python](https://github.com/alfredodeza/python-testing/)
- [Week 4: Introduction to Pandas and Numpy](https://github.com/alfredodeza/pandas-and-numpy)
- [Testing In Python book](https://learning.oreilly.com/library/view/testing-in-python/97986PAIML/)
- [Minimal Python book](https://www.amazon.com/Minimal-Python-efficient-programmer-onemillion2021-ebook/dp/B0855NSRR7)
- [Free Azure Certification for Students](https://docs.microsoft.com/learn/certifications/student-training-and-certification?WT.mc_id=academic-0000-alfredodeza)
- [Python for Beginners Learn Path](https://docs.microsoft.com/learn/paths/beginner-python/?WT.mc_id=academic-0000-alfredodeza)

### Course video and links

> 🎥 Click the image below to access Week 3 of the full course on O'Reilly

[![O'Reilly](https://learning.oreilly.com/covers/urn:orm:video:50146VIDEOPAIML/400w/)](https://learning.oreilly.com/videos/python-bootcamp-for/50146VIDEOPAIML/50146VIDEOPAIML-c1_s2/ "Introduction to Python")

This assignment is for Week 3 (out of 4) of the Python Bootcamp for Data. The whole course has four weeks:

- [week 1: Introduction to Python](https://github.com/alfredodeza/introduction-to-python)
- [Week 2: Python Functions and Classes](https://github.com/alfredodeza/python-functions-and-classes)
- [Week 3: Testing In Python](https://github.com/alfredodeza/python-testing/)
- [Week 4: Introduction to Pandas and NumPy](https://github.com/alfredodeza/pandas-and-numpy)

## Bonus challenge
Open the [bonus](./bonus) directory and then look into the [main.py](./bonus/main.py) file. It has several functions that could use some refactoring and unit tests. The tasks are marked with `#TODO` comments. Follow the instructions for each comment. This bonus assignment is not graded and will not trigger auto-grading. It is meant to be a challenge for you to practice what you learned in the course.
