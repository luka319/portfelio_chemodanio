package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(2015, 7, 14, 12, 26, 23, 0, time.Local) 
        // задаем первоначальную дату равную 14 июня 2015 года, 12:26:23

	fmt.Println(t.Format("2"))
	fmt.Println(t.Format("01"))
	fmt.Println(t.Format("06"))
	fmt.Println(t.Format("2006"))
	fmt.Println(t.Format("05"))
	fmt.Println(t.Format("15"))

	fmt.Println(t.Format("2.01.2006 15:04:05"))
	fmt.Println(t.Format("2 Jan 2006 year"))
	fmt.Println(t.Format("Monday"))
	fmt.Printf("%d days of %d year\n", t.YearDay(), t.Year())
}
