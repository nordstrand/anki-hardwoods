annotate ()
{
    width=`identify -format %w $1`
    convert -background '#0008' -fill white -gravity center -size ${width}x20 caption:"$2" $1 +swap -gravity south -composite $1
}
