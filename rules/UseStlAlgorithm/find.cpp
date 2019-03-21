
#include <vector>

bool f1(std::vector<int> v)
{
    int i = 0;
    int found = -1;
    for(const auto& x : v) {
        i++;
        if(x == 1) {
            found = i;
        }
    }
    return found > 0;
}

bool f2(std::vector<int> v)
{
    int i = 0;
    int found = -1;
    for(const auto& x : v) {
        i++;
        if(x == 1) {
            found = i;
            break;
        }
    }
    return found > 0;
}

bool f3(std::vector<int> v)
{
    int i = 0;
    int found = -1;
    for(const auto& x : v) {
        if(x == 1) {
            found = i;
        }
        i++;
    }
    return found > 0;
}

bool f4(std::vector<int> v)
{
    int i = 0;
    int found = -1;
    for(const auto& x : v) {
        if(x == 1) {
            found = i;
            break;
        }
        i++;
    }
    return found > 0;
}


