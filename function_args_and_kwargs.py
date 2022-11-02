def poem(data, *args, **kwargs):
    text = '\n'.join(args)
    information = '\n'.join([f'{key.title()}: {value}' for key, value in kwargs.items()])
    message = f'{data}\n\n{text}\n\n{information}'
    print(message)

poem(
    'Written in 1829 but was not published until after Poe\'s death.',
    'Edgar Allan Poe: Collected Works', 
    'Alone', 
    'From childhood\'s hour I have not been',
    'As others were—I have not seen',
    'As others saw—I could not bring',
    'My passions from a common spring—',
    'From the same source I have not taken',
    'My sorrow—I could not awaken',
    'My heart to joy at the same tone—',
    'And all I lov\'d—I lov\'d alone—',
    'Then—in my childhood—in the dawn',
    'Of a most stormy life—was drawn',
    'From ev\'ry depth of good and ill',
    'The mystery which binds me still—',
    'From the torrent, or the fountain—',
    'From the red cliff of the mountain—',
    'From the sun that \'round me roll\'d',
    'In its autumn tint of gold—',
    'From the lightning in the sky',
    'As it pass\'d me flying by—',
    'From the thunder, and the storm—',
    'And the cloud that took the form',
    '(When the rest of Heaven was blue)',
    'Of a demon in my view—',
    author='Edgar Allan Poe', 
    year=1829
)