# Example C# Formatting

This is an example of how we would like your C# code to be formatted.  Here you
will see code examples, in contrast to our [C# Style Guide](CSharpStyle.md)
which we like to keep short and concise.

These are _guidelines_, which mean that they describe how we would like your
code to be formatted such that they uphold the style guide. However, making
code is very much a creative process, and you are encouraged to find your own
way of expressing things (within the limits of what our Style Guide allows).

```csharp
using System;

namespace MyNamespace {
    public class MyClass<MyType> : IMyInterface {
        private int MyProperty { get; private set; }
        
        protected int myValue;
        
        public MyClass(int myValue) {
            this.myValue = myValue;
        }
        
        public override string ToString() {
            return String.Format("myValue: {0}", myValue);
        }
        
        public void MyInterfaceMethod(int arg1, int arg2) {
            if (myValue < arg1) {
                myValue += arg2;
            } else {
                myValue -= arg1;
            }
        }
    }
}
```
