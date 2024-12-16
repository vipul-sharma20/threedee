# threedee
Utility tool to work with some common STL modification recipes.

> [!NOTE]
> This will be mostly tailored to my personal 3D printing projects and to solve
> the problems I face. Some of these utilities may be helpful for some people

## Installation

```
pip install https://github.com/vipul-sharma20/threedee/releases/download/v0.2.0/threedee-0.2.0-py3-none-any.whl
```

## Usage

### GitHub Skyline
```
threedee github-skyline --width=<width> --stl-path=<path> --username=<username> --start=<start-year> --end=<end-year>
```

This can be used to combine multiple years of [GitHub Skylines][github-skyline] into a one single print.

> [!NOTE]
> GitHub has released a CLI tool (after I had solved it for myself) called,
> [gh-skyline][gh-skyline] which is quite similar. I think my render is still a
> little better in terms of portability.

Below is a sample of my last 10 years of GitHub Skylines combined

[View STL File](https://gist.github.com/vipul-sharma20/427bcd96d9899906ff6ca2dd40ba3421#github.stl)

**📷 Preview**

![STL Preview](https://i.imgur.com/qnjRL0D.png)


[github-skyline]: https://skyline.github.com/
[gh-skyline]: https://github.com/github/gh-skyline
