
# Linux

    $ git config --global alias.shrine '!git commit -m "$(curl -s http://shrine.duckdns.org/shrine.txt)"'

# Windows

    X:\> git config --global alias.shrine "!curl -s -O http://shrine.duckdns.org/shrine.txt; git commit -F shrine.txt; rm shrine.txt"