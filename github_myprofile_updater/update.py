if __name__ == '__main__':
    _header = '## Hi there 👋\n![](https://komarev.com/ghpvc/?username=yang-ze-kang&color=green)'
    base_dir = '../_pages/includes/'
    _intro = open(f'{base_dir}/intro.md').read().strip()
    # _homepage = open(f'{base_dir}/homepage.md').read().strip()
    _pub = open(f'{base_dir}/pub.md').read().strip()
    # _news = open(f'{base_dir}/news.md').read().strip()
    _starts = open(f'{base_dir}/starts.md').read().strip()
    with open('README.md', 'w') as f:
        f.write(_header)
        f.write('\n\n')
        f.write(_intro)
        # f.write('\n\n##')
        # f.write(_homepage)
        f.write('\n\n##')
        # f.write(_news)
        f.write('\n\n##')
        f.write(_pub)
        f.write('\n\n')
        f.write(_starts)