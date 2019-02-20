from html.parser import HTMLParser

meta_count = 0


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def handle_comment(self, data):
        # called when comment is encountered
        print("Encountered comment", data)
        pos = self.getpos()  # returns line and position of comment
        print("\tAt line:", pos[0], "position", pos[1])

    def handle_starttag(self, tag, attrs):
        # function called when entire stag tag is read including attributes
        global meta_count
        if tag == 'meta':
            meta_count += 1
        print("Encountered start tag", tag)
        pos = self.getpos()
        # returns line and position of comment
        print("\tAt line:", pos[0], "position", pos[1])

        if attrs.__len__() > 0:
            print("\tAtttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_endtag(self, tag):
        print("Encountered end tag", tag)
        pos = self.getpos()  # returns line and position of comment
        print("\tAt line:", pos[0], "position", pos[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered data", data)
        pos = self.getpos()  # returns line and position of comment
        print("\tAt line:", pos[0], "position", pos[1])


def main():
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == 'r':  # file successfully opened
        contents = f.read()
        parser.feed(contents)

    print("Meta tags found", meta_count)


if __name__ == '__main__':
    main()
