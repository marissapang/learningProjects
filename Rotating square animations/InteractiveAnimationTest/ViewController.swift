//
//  ViewController.swift
//  InteractiveAnimationTest
//
//  Created by apple on 6/7/20.
//  Copyright © 2020 KnowledgeIsBacon. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var boxView: UIView?
    var angle: Double = 180
    var scaleFactor: CGFloat = 2

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let frameRect = CGRect(x: 50, y: 50, width: 50, height: 50)
        boxView = UIView(frame: frameRect)
        boxView?.backgroundColor = UIColor.blue
        self.view.addSubview(boxView!)
        
        
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        if let touch = touches.first {
            let location = touch.location(in: self.view)
            //let timing = UICubicTimingParameters(animationCurve: .easeInOut)
            let timing = UISpringTimingParameters(mass: 0.5, stiffness: 0.5, damping: 0.3, initialVelocity: CGVector(dx:1.0, dy: 0.0))
            let animator = UIViewPropertyAnimator(duration: 2.0, timingParameters: timing)

            animator.addAnimations {
                let scaleTrans = CGAffineTransform(scaleX: self.scaleFactor, y: self.scaleFactor)
                let rotateTrans = CGAffineTransform(rotationAngle: CGFloat(self.angle * Double.pi / 180))
                self.boxView?.transform = scaleTrans.concatenating(rotateTrans)
                self.angle = (self.angle == 180 ? 360 : 180)
                self.scaleFactor = (self.scaleFactor == 2 ? 1 : 2)
                self.boxView?.backgroundColor = UIColor.purple
                self.boxView?.center = location
            }

            animator.addCompletion {
                _ in self.boxView?.backgroundColor = UIColor.green
            }
            animator.startAnimation()
        }
    }


}

