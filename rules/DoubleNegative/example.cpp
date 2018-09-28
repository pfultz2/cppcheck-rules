void example(bool b)
{
    int b1 = !!b;
    int b2 = ~~b;
    int b3 = !(!b);
    int b4 = ~(~b);
    (void)b1;
    (void)b2;
    (void)b3;
    (void)b4;
}
