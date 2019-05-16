dir="/Users/mirkovelimirovic/Documents/GitHub/karmilla/fonts"

ttfs="$(ls $dir/*/*.ttf)"
echo $ttfs

for ttf in $ttfs; do
    woff2_compress $ttf
    echo "Build woff2 for $ttf"
done
