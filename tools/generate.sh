DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

find $DIR | grep "in$" | sed 's/.in$//g' | xargs -n 1 -P 8 -I{} -t bash -c "python $DIR/{}.in > $DIR/{}.xml"
