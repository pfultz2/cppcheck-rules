DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

cat $(find $DIR/rules | grep "rule.xml") | grep -v -F '<?xml'
