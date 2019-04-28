
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

bool f5(std::vector<int> v)
{
    int i = 0;
    int found = -1;
    for(const auto& x : v) {
        if(x == 1) {
            found = i;
            return true;
        }
        i++;
    }
    return found > 0;
}

int f6(A a, int x)
{
    int i = 0;
    for(auto&& y : a->f().g())
    {
        if(y == x)
            return i;
        i++;
    }
    return -1;
}
