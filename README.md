# wp-img-src-to-table

**This is modified version of [Eli Williams' awesome script](https://elitwilliams.medium.com/check-for-404-rrors-in-bulk-using-this-simple-python-script-and-a-list-of-urls-cf3cf6a97eca)**

I added xml parsing feature so that **you can now check WordPress backup file!**

## Usage

**BEFORE USING THIS SCRIPT, please replace `content:encoded` with `content` in order to avoid syntax error when parsing xml.

```
if __name__ == "__main__":
    main('test.xml','result.txt')
```

Then, **c**hange file names** into like 'WordPress.xxxx-xx-xx.xml'.

![table.png](https://github.com/and0ry0/wp-img-src-to-table/blob/main/README/table.png?raw=true)

Then, run `convert.py` and check `result.txt`. **Copy and paste the text into Excel or SpreadSheets etc.** and you can find missing images.