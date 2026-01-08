text = input()
if text.startswith('IMG_') and text.endswith('.png') or text.endswith('.jpg'):
    print('File is correct')
else:
    print('File is not correct')