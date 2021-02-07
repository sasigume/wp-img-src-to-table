import requests
import untangle
import re


def get_url_status(urls,file):
    f = open(file, 'a')

    for url in urls:
        try:
            r = requests.get(url)
            f.write(url + "\tSUCCESS:\t" + str(r.status_code) + "\n")
        except Exception as e:
            print('Error: ' + e)
            f.write(url + "\tERROR:\t" + str(e) + "\n")
    return None


def main(source,output):
    print('Parsing xml...')
    obj = untangle.parse(source)
    content = ",".join([item.content.cdata for item in obj.rss.channel.item])
    exp = re.compile('<img\s+[^>]*?src="(.+?)"')
    urls = re.findall(exp, content)
    print('Got urls')
    get_url_status(urls,output)
    print('Succeed!')


if __name__ == "__main__":
    main('test.xml','result.txt')
