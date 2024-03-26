with open('dummy.txt','r') as reader:
    content = reader.readlines()
    with open('newfile.txt','a') as writer:
        for line in reversed(content):
            writer.writelines(line)