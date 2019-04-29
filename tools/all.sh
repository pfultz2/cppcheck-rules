DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

EXCULDE=$1
if [ -z "$EXCULDE" ]
then
    FILES=$(find $DIR/rules | grep "rule.xml")
else
    FILES=$(find $DIR/rules | grep "rule.xml" | grep -v "$1")
fi

cat $FILES | grep -v -F '<?xml'
