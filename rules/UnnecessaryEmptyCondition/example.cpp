void f(std::vector<int> v)
{
    if (v.empty())
    {
        for(auto&& x:v)
        {}
    }
}

void f(std::vector<int> v)
{
    if (!v.empty())
    {
        for(auto&& x:v)
        {}
    }
}
