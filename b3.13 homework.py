class HTML:
    def __init__(self, output = None):
        self.output = output
        self.childrens = []
    
    def __enter__(self):
        return self
    
    def __add__(self, other):
        self.childrens.append(other)
        return self
    
    def __exit__(self, *args):
        print("<html>")
        for child in self.childrens:
            print(str(child))
    
        print("</html>")

class TopLevelTag:
    def __init__(self, tag):
        self.tag = tag
        self.childrens = []

    def __enter__(self):
        return self

    def __add__(self, other):
        return TopLevelTag(self.childrens.append(other))

    def __str__(self):
        print("<{tag}>".format(tag = self.tag))
        for child in self.childrens:
            print(str(child))
        print("</{tag}>".format(tag = self.tag))

    def __exit__(self, *attrs):
        return self
class Tag:
    def __init__(self, tag, is_single = False, **atrs):
        self.tag = tag
        self.text = ""
        self.is_single = is_single
        self.attributes = atrs

    def __enter__(self):
        return self

    def __exit__(self, *atrs):
        return self

    def __str__(self):
        attrs = []
        for key, value in self.attributes.items:
            attrs.append('{key}="{value}"'.format(key, value))
        attr_string = " ".join(attrs)
        if self.is_single:
            print("<{tag} {attrs}/>".format(tag = self.tag, attrs = attr_string))
        else:
            print("<{tag} {attrs}>{text}</{tag}>".format(tag = self.tag, attrs = attr_string, text = self.text))

if __name__ == "__main__":
    with HTML(output=None) as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "hello"
                head += title
            doc += head

        with TopLevelTag("body") as body:
            with Tag("h1", klass=("main-text",)) as h1:
                h1.text = "Test"
                body += h1

            with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                with Tag("p") as paragraph:
                    paragraph.text = "another test"
                    div += paragraph

                with Tag("img", is_single=True, src="/icon.png") as img:
                    div += img

                body += div

            doc += body            