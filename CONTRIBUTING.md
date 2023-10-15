# Contributing to ColorCompass

First off, thank you for considering contributing to ColorCompass! 🎨🧭 It's people like you that make ColorCompass such a great tool.

## Where do I go from here?

If you've noticed a bug or have a question, [search the issue tracker](https://github.com/NicolasAguirreCampi/ColorCompass/issues) to see if someone else in the community has already created a ticket. If not, go ahead and [make one](https://github.com/NicolasAguirreCampi/ColorCompass/issues/new)!

## Fork & create a branch

If this is something you think you can fix, then [fork ColorCompass](https://help.github.com/articles/fork-a-repo) and create a branch with a descriptive name.

A good branch name would be (where issue #XX is the ticket you're working on):

```sh
git checkout -b fix-XX-description-of-fix
```

## Implement your fix or feature

At this point, you're ready to make your changes!

## Get the style right

Your patch should follow the same conventions & pass the same code quality checks as the rest of the project. 

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with ColorCompass’s master branch:

```sh
git remote add upstream git@github.com:NicolasAguirreCampi/ColorCompass.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master and push it!

```sh
git checkout fix-XX-description-of-fix
git rebase master
git push --set-upstream origin fix-XX-description-of-fix
```

And [submit a pull request](https://github.com/NicolasAguirreCampi/ColorCompass/compare) on GitHub.

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of [good](https://stackoverflow.com/questions/6223074/git-rebase-in-plain-english) [resources](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) but here's the suggested workflow:

```sh
git checkout fix-XX-description-of-fix
git pull --rebase upstream master
git push --force-with-lease origin fix-XX-description-of-fix
```