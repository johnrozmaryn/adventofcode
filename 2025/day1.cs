using System;

Console.WriteLine("Hello, World!");

string contents = File.ReadAllText("day01.tst");
List<string> lines = contents.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries).ToList();
foreach (string i in lines) {
    Console.WriteLine(i);
}
