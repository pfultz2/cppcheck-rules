void example()
{
    for (int i = 0; i < 10; i++)
    {
        if (foo(i))
        {
            continue;
        }
        break;      // this break is confusing
    }
}
