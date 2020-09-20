//
//  ViewController.swift
//  fives tile animation test
//
//  Created by apple on 6/10/20.
//  Copyright © 2020 KnowledgeIsBacon. All rights reserved.
//

import UIKit

enum AnimationDirection: Int {
    case up, down, left, right, undefined
}


class ViewController: UIViewController {
    //MARK: Properties
    var tileView = UIView(frame: CGRect(x: 30, y: 100, width: 50, height: 65))
    var tileView2 = UIView(frame: CGRect(x: 30, y: 100, width: 50, height: 65))
    let dimensions : Int = 4
    let spacing : CGFloat = 60
    var animator = UIViewPropertyAnimator()
    var animator2 = UIViewPropertyAnimator()
    
    var currentColIndex : Int = 0
    var currentRowIndex : Int = 0
    var currentColIndex2 : Int = 2
    var currentRowIndex2 : Int = 2
    
    //MARK: Override funcs

    override func viewDidLoad() {
        super.viewDidLoad()
        tileView.backgroundColor = UIColor.blue
        tileView2.backgroundColor = UIColor.red
        self.view.addGestureRecognizer(panRecognizer)
        self.view.addSubview(tileView)
        self.view.addSubview(tileView2)
    }
    
//    func loop(){
//        var view : UIView
//        for i in 0..<2 {
//            view = tileView
//
//        }
//    }
        
    
    //MARK: Pan functions
    @objc private func handlePan(recognizer: UIPanGestureRecognizer) {
        var direction : AnimationDirection

        switch recognizer.state {
        case .began:
            direction = directionFromVelocity(recognizer.velocity(in: self.view))
            
            switch direction {
            case .left:
                currentColIndex = max(currentColIndex-1, 0)
                currentColIndex2 = max(currentColIndex2-1, 0)
            case .right:
                currentColIndex = min(currentColIndex+1, dimensions-1)
                currentColIndex2 = min(currentColIndex2+1, dimensions-1)
            case .up:
                currentRowIndex = max(currentRowIndex-1, 0)
                currentRowIndex2 = max(currentRowIndex2-1, 0)
            case .down:
                currentRowIndex = min(currentRowIndex+1, dimensions-1)
                currentRowIndex2 = min(currentRowIndex2+1, dimensions-1)
            default:
                ()
            }
                        
            animator = UIViewPropertyAnimator(duration: 1, curve: .easeInOut, animations: {
                self.tileView.transform = CGAffineTransform(translationX: self.spacing * CGFloat(self.currentColIndex), y: self.spacing * CGFloat(self.currentRowIndex))
            })
            
            animator2 = UIViewPropertyAnimator(duration: 1, curve: .easeInOut, animations: {
                self.tileView2.transform = CGAffineTransform(translationX: self.spacing * CGFloat(self.currentColIndex2), y: self.spacing * CGFloat(self.currentRowIndex2))
            })
            
            animator.startAnimation()
            animator.pauseAnimation()
            animator2.startAnimation()
            animator2.pauseAnimation()
        case .changed:
            direction = directionFromVelocity(recognizer.velocity(in: tileView))
            switch direction {
            case .left, .right:
                animator.fractionComplete = abs(recognizer.translation(in: tileView).x) / spacing
                animator2.fractionComplete = abs(recognizer.translation(in: tileView2).x) / spacing
            case .up, .down:
                animator.fractionComplete = abs(recognizer.translation(in: tileView).y) / spacing
                animator2.fractionComplete = abs(recognizer.translation(in: tileView2).y) / spacing
            default:
                ()
            }
        case .ended:
            print("ending fraction complete is \(animator.fractionComplete) and \(animator2.fractionComplete)")
            if animator.fractionComplete < 0.2 {
                animator.isReversed = true
                animator2.isReversed = true
            } else {
                animator.isReversed = false
                animator2.isReversed = false
            }
            animator.continueAnimation(withTimingParameters: nil, durationFactor: 0)
            animator2.continueAnimation(withTimingParameters: nil, durationFactor: 0)
        default:
            ()
        }
    }
    
    private func directionFromVelocity(_ velocity: CGPoint) -> AnimationDirection {
        guard velocity != .zero else { return .undefined }
        let isVertical = abs(velocity.y) > abs(velocity.x)
        var derivedDirection: AnimationDirection = .undefined
        if isVertical {
            derivedDirection = velocity.y < 0 ? .up : .down
        } else {
            derivedDirection = velocity.x < 0 ? .left : .right
        }
        return derivedDirection
    }
    
    private lazy var panRecognizer: UIPanGestureRecognizer = {
        let recognizer = UIPanGestureRecognizer()
        recognizer.addTarget(self, action: #selector(handlePan(recognizer:)))
        return recognizer
    }()


}

