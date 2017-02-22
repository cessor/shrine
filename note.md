
# Linux

    $ git config --global alias.shrine '!git commit -m "$(curl -s http://shrine.duckdns.org/shrine.txt)"'

# Windows

    curl -s http://shrine.duckdns.org/shrine.txt > shrine.txt & git commit -F shrine.txt & rm shrine.txt