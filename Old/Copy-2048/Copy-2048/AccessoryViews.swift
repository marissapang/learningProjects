//
//  AccessoryViews.swift
//  Copy-2048
//
//  Created by apple on 5/20/20.
//  Copyright © 2020 MP. All rights reserved.
//

import UIKit

protocol ScoreViewProtocol {
    func scoreChanged(to s: Int)
}

/// A simple view that displays the player's score
class ScoreView : UIView, ScoreViewProtocol {
    var score : Int = 0 {
        didSet {
            label.text = "SCORE: \(score)"
        }
    }
    
    let defaultFrame  = CGRect(x: 0, y: 0, width: 140, height: 40)
    var label: UILabel
    
    init(backgroundColor bgcolor: UIColor, textColor tcolor: UIColor, font: UIFont, radius r: CGFloat){
        label = UILabel(frame: defaultFrame)
        label.textAlignment = NSTextAlignment.center
        super.init(frame: defaultFrame)
        backgroundColor = bgcolor
        label.textColor = tcolor
        label.font = font
        layer.cornerRadius = r
        self.addSubview(label)
    }
    
    required init(coder Adecoder: NSCoder){
        fatalError("NSCoding not supported")
    }
    
    func scoreChanged(to s: Int){
        score = s
    }
}

// A simple view that displays several buttons for controlling the app
class ControlView {
  let defaultFrame = CGRect(x: 0, y: 0, width: 140, height: 40)
  // TODO: Implement me
}
