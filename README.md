# Intern Skills

A Silverpond intership is not just getting coffee! You will be working
on active projects that will be incorporated into Silverpond's core codebase.

In order to be productive we have identified a set of core skills we
expect any intern to be proficent in when they start.

This repo is to help potenial interns self assess and practice these
core skills:

  1. **Python**: Internally we use Python > 3.11. We expect any intern to have coded at least a small project in Python before. Creating a Github account for your code including the link in your application will go a long way towards demonstrating your proficiency in both Python and Github. If you can flex any other programming language skills in this repo that's a bonus!
  2. **Python environment basics**: Typically a Python project runs in it’s own environment with it’s own dependencies specified in a configuration file, like; `requirements.txt` or `pyproject.toml`. If you're used to Conda that's ok too.
  3. **Unix Terminal**: Our development machines (The ones with the big GPUS) all run a Linux based OS called NixOS (for what you'll be doing, just think; Ubuntu). You will be expected to access one of these machines remotely over ssh to do some development. We expect you to be able to navigate around, create, move, copy and remove files and directories confidently. See [this](https://www.youtube.com/watch?v=5jIIOkA0NpI&list=PLKp3X-578hN99d7bj6EU-AnGyAE6Fdc6R&index=2) YouTube video if you need to learn these skills.
  4. **Git**: Source control using Git is a cornerstone of most jobs involving software development. A non-exhaustive list of common git commands you should be familiar with is; `clone, pull, push, fetch, merge, checkout, rebase`. We also expect you to be using `ssh` authentication not `https`. There are lots of great resources online to brush up on your Git skills if you need to.
  5. **Vim/Neo-VIM**:  You may use VSCode or some other IDE for your Python development. Many IDEs provide plugins for remote development over ssh. But it is inevitable you’ll find yourself in a Vim editor at some point. Don’t be one of [over 1 million developers](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/) that have Googled this in past. Learn some vim! Either on [YouTube](https://www.youtube.com/watch?v=IiwGbcd8S7I) or in the built-in `vimtutor` that is on most Unix machines.
  6. **Remove Development**: We have mentioned remote development a lot. You will need to have an ssh key pair setup on your machine so we can copy your private key to our development machines to allow you access. This is the same public ssh key you would likely need to add to your github account to enable ssh authentication.
  7. GET A PASSWORD MANAGER AND USE IT!

## Your Task

  1. Clone this repo
  2. Create a python virtual environment and install the dependancies in `requirements-cpu.txt`
  3. Run the Jupyer [pytorch_mnist notebook](notebooks/pytorch_mnist.ipynb) in your virtual environment.
  4. Identify/Fix the issues (one or more cells will fail, you'll need to fix them)
  5. Create a Pull Request with your fix
    - Use the command `nbstripout notebooks/pytorch_mnist.ipynb` before adding the fixed notebook to your commit. This will clear the output cells so only the code and text cells remain.

Once you're confident you can complete the task take a screen recording of 
youself doing it and talking us through it.

### What We're Assessing

  - Your confidence using common tools Git, Python, virtual envs
  - Your ability to communicate what you're thinking when working through 
  problem. This will require you to explain what you're doing during the 
  screen recording. **Videos with no explanations will be an automatic 'No'**

We will **NOT** be assessing your video production/editing skills! Provided we 
can see what you're doing and hear your explanations that's great.

