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
    let dimensions : Int = 4
    let spacing : CGFloat = 60
    var animator = UIViewPropertyAnimator()
    
    var currentColIndex : Int = 0
    var currentRowIndex : Int = 0
    
    //MARK: Override funcs

    override func viewDidLoad() {
        super.viewDidLoad()
        tileView.backgroundColor = UIColor.blue
        tileView.addGestureRecognizer(panRecognizer)
        self.view.addSubview(tileView)
    }
        
    
    //MARK: Pan functions
    @objc private func handlePan(recognizer: UIPanGestureRecognizer) {
        var direction : AnimationDirection

        switch recognizer.state {
        case .began:
            direction = directionFromVelocity(recognizer.velocity(in: tileView))
            
            switch direction {
            case .left:
                currentColIndex = max(currentColIndex-1, 0)
            case .right:
                currentColIndex = min(currentColIndex+1, dimensions-1)
            case .up:
                currentRowIndex = max(currentRowIndex-1, 0)
            case .down:
                currentRowIndex = min(currentRowIndex+1, dimensions-1)
            default:
                ()
            }
            
            print(currentColIndex)
            
            animator = UIViewPropertyAnimator(duration: 1, curve: .easeInOut, animations: {
                self.tileView.transform = CGAffineTransform(translationX: self.spacing * CGFloat(self.currentColIndex), y: self.spacing * CGFloat(self.currentRowIndex))
            })
        
            
            animator.startAnimation()
            animator.pauseAnimation()
        case .changed:
            direction = directionFromVelocity(recognizer.velocity(in: tileView))
            switch direction {
            case .left, .right:
                animator.fractionComplete = abs(recognizer.translation(in: tileView).x) / spacing * max(1, CGFloat(self.currentColIndex))
            case .up, .down:
                animator.fractionComplete = abs(recognizer.translation(in: tileView).y) / spacing * max(1, CGFloat(self.currentRowIndex))
            default:
                ()
            }
//            animator.fractionComplete = abs(recognizer.translation(in: tileView).x) / spacing * max(1, CGFloat(self.currentColIndex))
        case .ended:
            if animator.fractionComplete < 0.1 {
                animator.isReversed = true
            } else {
                animator.isReversed = false
            }
            animator.continueAnimation(withTimingParameters: nil, durationFactor: 0)
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

