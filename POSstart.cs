using System;
using System.Drawing;
using System.Drawing.Printing;

class Program
{
    static void Main()
    {
        string textToPrint = "This is a test string to print.";

        PrintDocument printDocument = new PrintDocument();
        printDocument.PrintPage += (sender, args) =>
        {
            args.Graphics.DrawString(textToPrint, new Font("Arial", 12), Brushes.Black, new RectangleF(0, 0, printDocument.DefaultPageSettings.PrintableArea.Width, printDocument.DefaultPageSettings.PrintableArea.Height));
        };

        try
        {
            printDocument.Print();
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred while printing: " + ex.Message);
        }
    }
}
