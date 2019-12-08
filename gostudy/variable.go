package main
import "fmt"
func main() {
    var a  = "hello world"
    fmt.Println(a)

    b := "go go go"
    c := b
    fmt.Println(c)
    fmt.Println(&c)
    fmt.Println(&b)

    //var b int
    //fmt.Println(b)

    //var c bool 
    //fmt.Println(c)
}
