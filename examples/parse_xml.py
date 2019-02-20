import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse("samplexml.xml")
    print(type(doc))
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    make = doc.getElementsByTagName("make")
    print("%d make" % make.length)
    for m in make:
        print(m.getAttribute("name"))
    new_skill = doc.createElement("skill")
    new_skill.setAttribute("name", "fighter")
    doc.firstChild.appendChild(new_skill)


if __name__ == '__main__':
    main()
