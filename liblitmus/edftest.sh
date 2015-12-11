# ! /bin/zsh

sudo ./rtspin -f test/41.csv -p 1 -C 0 -w -q 1 8 42 8 42 &
sudo ./rtspin -f test/42.csv -p 1 -C 0 -w -q 2 4 62 4 62 &
sudo ./rtspin -f test/43.csv -p 1 -C 1 -w -q 3 4 48 10 48 &
sudo ./rtspin -f test/44.csv -p 1 -C 1 -w -q 4 8 32 12 32 &

