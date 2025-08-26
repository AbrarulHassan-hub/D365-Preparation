// See https://aka.ms/new-console-template for more information

/*-------------------Abstraction START----------
Animal dog = new Dog();
dog.MakeSound();
dog.Sleep();
Animal c = new Cat();
c.Sleep();
c.MakeSound();
public abstract class Animal
{
    public abstract void MakeSound();
    public void Sleep()
    {
        Console.WriteLine("Animal is Sleeping");
    }
}
public class Dog:Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Dog barking");
    }
}
public class Cat: Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Cat Meows");
    }
}
*/
/*-------------------Abstraction END----------
 




//-----------------PolyMorphsim----------------
/*

Ploymorphsim : Yani ek hi method ka different behavior alag-alag classes me.
Polymorphism do types ka hota hai:
Compile - time Polymorphism(Method Overloading)
Run - time Polymorphism(Method Overriding)
------Compile-time Polymorphism (Method Overloading)----------

Calculator c = new Calculator();
c.Add(3, 4);
c.Add(3, 5, 6);
public class Calculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }
    public int Add(int a, int b, int c)
    {
        return a + b + c;
    }
}

//--------Run-time Polymorphism (Method Overriding)----------

Animal a = new Animal();
a.speak();
Animal d = new Dog();
d.speak();
public class Animal
{
    public virtual void speak()
    {
        Console.WriteLine("Animals Makes Sound");
    }
}
public class Dog:Animal
{
    public override void speak()
    {
        Console.WriteLine("Dog Bark");
    }
}
*/
//-----------------PolyMorphsim END----------------




/*
 //------------Hierarchical Inheritance------------------
Dog dog = new Dog();
dog.Eat();   // From Animal
dog.Bark();  // Dog’s own method

Cat cat = new Cat();
cat.Eat();   // From Animal
cat.Meow();  // Cat’s own method

Cow cow = new Cow();
cow.Eat();   // From Animal
cow.Moo();   // Cow’s own method


public class Animal
{
    public void Eat()
    {
        Console.WriteLine("All animals eat food.");
    }
}

// Child Class 1
public class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Dog barks.");
    }
}

// Child Class 2
public class Cat : Animal
{
    public void Meow()
    {
        Console.WriteLine("Cat meows.");
    }
}

// Child Class 3
public class Cow : Animal
{
    public void Moo()
    {
        Console.WriteLine("Cow moos.");
    }
}




//-----MultiLevel Inheritance
Dog d = new Dog();
d.Breathe();
d.Eat();
d.Bark();

 public class LivingBeing
{
    public void Breathe()
    {
        Console.WriteLine("Living Being breathe!");
    }
}
public class Animal:LivingBeing
{
    public void Eat()
    {
        Console.WriteLine("Animals Eat Foood");
    }
}
public class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Gog Barks!");
    }
}

//------------ Single Level Inheritance ---------
Dog d = new Dog();
d.Eat();
d.Bark();
public class Animal
{
    
    public void Eat()
    {
        Console.WriteLine("Animals Eat Food");
    }
}
public class Dog:Animal
{
    public void Bark()
    {
        Console.WriteLine("Dog Bark!");
    }
}
*/
//------------Hierarchical Inheritance END------------------





/*
//----------------Encapsulation--------------------
BankAmount ba = new BankAmount();
ba.DepositeAmount(50000);
ba.Balance = 50000;
public class BankAmount
{
    private double balance;
    public double Balance
    {
        get { return balance; }
        set { balance = value; }
    }
    public void DepositeAmount(double amount)
    {
        if(amount > 0)
        {
            balance = balance + amount;
            Console.WriteLine("Blance Amount " + balance);
        }
        else
        {
            Console.WriteLine("Invalid Deposite Amount");
        }
    }
    public void withDraw(double amount)
    {
        if(amount > 0 && amount < balance)
        {
            balance = balance - amount;
            Console.WriteLine($"WidthDraw Amount ");
        }
    }
}
//----------------Encapsulation END--------------------
*/
