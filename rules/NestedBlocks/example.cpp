int f1(int x)
{
    if (x) {
        { return x; }
    }
    return 0;
}
void f2(int x)
{
    switch (x)
    {
        case 1: break;
        case 2: {} break;
        case 3:
        { // expected-error {{block directly inside block [loplugin:blockblock]}}
            {
            }
            break;
        }
    }
}