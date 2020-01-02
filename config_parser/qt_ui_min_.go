// https://github.com/visualfc/goqt/blob/master/examples/minimal/main.go

// go get "github.com/visualfc/goqt/ui"

package main

import "github.com/visualfc/goqt/ui"

func main() {
	ui.Run(func() {
		widget := ui.NewWidget()
		widget.Show()
	})
}
